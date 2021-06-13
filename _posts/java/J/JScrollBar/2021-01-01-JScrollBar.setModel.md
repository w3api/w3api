---
title: JScrollBar.setModel()
permalink: /Java/JScrollBar/setModel/
date: 2021-01-11
key: Java.J.JScrollBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.metodos valor="setModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, description="The scrollbar\'s BoundedRangeModel.") public void setModel(BoundedRangeModel newModel)
~~~

## Parámetros
* **BoundedRangeModel newModel**,  {% include w3api/param_description.html metodo=_dato parametro="BoundedRangeModel newModel" %}

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
