---
title: JComponent.setMinimumSize()
permalink: /Java/JComponent/setMinimumSize/
date: 2021-01-11
key: Java.J.JComponent
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="setMinimumSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="The minimum size of the component.") public void setMinimumSize(Dimension minimumSize)
~~~

## Parámetros
* **Dimension minimumSize**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension minimumSize" %}

## Clase Padre
[JComponent](/Java/JComponent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
