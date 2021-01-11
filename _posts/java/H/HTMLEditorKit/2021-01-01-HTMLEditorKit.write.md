---
title: HTMLEditorKit.write()
permalink: Java/HTMLEditorKit/write
date: 2021-01-11
key: JavaJava.H.HTMLEditorKit
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLEditorKit.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(Writer out, Document doc, int pos, int len) throws IOException, BadLocationException
~~~

## Parámetros
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_dato parametro="Document doc" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_dato parametro="Writer out" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLEditorKit](/Java/HTMLEditorKit/)

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
