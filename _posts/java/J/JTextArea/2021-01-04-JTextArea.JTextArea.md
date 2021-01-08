---
title: JTextArea.JTextArea()
permalink: Java/JTextArea/JTextArea
date: 2021-01-04
key: JavaJava.J.JTextArea
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.constructores valor="JTextArea" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JTextArea()
public JTextArea(int rows, int columns)
public JTextArea(String text)
public JTextArea(String text, int rows, int columns)
public JTextArea(Document doc)
public JTextArea(Document doc, String text, int rows, int columns)
~~~

## Parámetros
* **int columns**,  {% include w3api/param_description.html metodo=_data parametro="int columns" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **int rows**,  {% include w3api/param_description.html metodo=_data parametro="int rows" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_data parametro="Document doc" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextArea](/Java/JTextArea/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JTextArea.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
