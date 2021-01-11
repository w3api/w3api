---
title: HTMLWriter.emptyTag()
permalink: Java/HTMLWriter/emptyTag
date: 2021-01-11
key: JavaJava.H.HTMLWriter
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLWriter.metodos valor="emptyTag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void emptyTag(Element elem) throws BadLocationException, IOException
~~~

## Parámetros
* **Element elem**,  {% include w3api/param_description.html metodo=_dato parametro="Element elem" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

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
