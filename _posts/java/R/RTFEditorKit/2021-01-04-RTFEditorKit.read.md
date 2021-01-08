---
title: RTFEditorKit.read()
permalink: Java/RTFEditorKit/read
date: 2021-01-04
key: JavaJava.R.RTFEditorKit
category: java
tags: ['java se', 'javax.swing.text.rtf', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RTFEditorKit.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void read(InputStream in, Document doc, int pos) throws IOException, BadLocationException
public void read(Reader in, Document doc, int pos) throws IOException, BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_data parametro="Reader in" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_data parametro="Document doc" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[RTFEditorKit](/Java/RTFEditorKit/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RTFEditorKit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
