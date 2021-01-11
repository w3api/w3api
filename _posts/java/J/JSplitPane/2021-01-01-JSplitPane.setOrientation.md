---
title: JSplitPane.setOrientation()
permalink: Java/JSplitPane/setOrientation
date: 2021-01-11
key: JavaJava.J.JSplitPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JSplitPane.metodos valor="setOrientation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(enumerationValues={"JSplitPane.HORIZONTAL_SPLIT","JSplitPane.VERTICAL_SPLIT"}, description="The orientation, or how the splitter is divided.") public void setOrientation(int orientation)
~~~

## Parámetros
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}

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
