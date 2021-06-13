---
title: JSplitPane.setResizeWeight()
permalink: /Java/JSplitPane/setResizeWeight/
date: 2021-01-11
key: Java.J.JSplitPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JSplitPane.metodos valor="setResizeWeight" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Specifies how to distribute extra space when the split pane resizes.") public void setResizeWeight(double value)
~~~

## Parámetros
* **double value**,  {% include w3api/param_description.html metodo=_dato parametro="double value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JSplitPane](/Java/JSplitPane/)

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
