---
title: TextField.TextField()
permalink: Java/TextField-java-awt/TextField
date: 2021-01-04
key: JavaJava.T.TextField-java-awt
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextField-java-awt.constructores valor="TextField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TextField() throws HeadlessException
public TextField(int columns) throws HeadlessException
public TextField(String text) throws HeadlessException
public TextField(String text, int columns) throws HeadlessException
~~~

## Parámetros
* **int columns**,  {% include w3api/param_description.html metodo=_data parametro="int columns" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[TextField](/Java/TextField-java-awt/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextField-java-awt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
