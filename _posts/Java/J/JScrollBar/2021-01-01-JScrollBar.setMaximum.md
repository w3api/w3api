---
title: JScrollBar.setMaximum()
permalink: /Java/JScrollBar/setMaximum/
date: 2021-01-11
key: Java.J.JScrollBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.metodos valor="setMaximum" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, preferred=true, description="The scrollbar\'s maximum value.") public void setMaximum(int maximum)
~~~

## Parámetros
* **int maximum**,  {% include w3api/param_description.html metodo=_dato parametro="int maximum" %}

## Clase Padre
[JScrollBar](/Java/JScrollBar/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
