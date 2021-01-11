---
title: ScrollPane.ScrollPane()
permalink: Java/ScrollPane-java-awt/ScrollPane
date: 2021-01-11
key: JavaJava.S.ScrollPane-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScrollPane-java-awt.constructores valor="ScrollPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScrollPane() throws HeadlessException
@ConstructorProperties("scrollbarDisplayPolicy") public ScrollPane(int scrollbarDisplayPolicy) throws HeadlessException
~~~

## Parámetros
* **int scrollbarDisplayPolicy**,  {% include w3api/param_description.html metodo=_dato parametro="int scrollbarDisplayPolicy" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScrollPane](/Java/ScrollPane-java-awt/)

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
