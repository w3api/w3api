---
title: HTMLWriter.output()
permalink: Java/HTMLWriter/output
date: 2021-01-11
key: JavaJava.H.HTMLWriter
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLWriter.metodos valor="output" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void output(char[] chars, int start, int length) throws IOException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **char[] chars**,  {% include w3api/param_description.html metodo=_dato parametro="char[] chars" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[HTMLWriter](/Java/HTMLWriter/)

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
