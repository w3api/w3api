---
title: HTMLEditorKit.read()
permalink: Java/HTMLEditorKit/read
date: 2021-01-04
key: JavaJava.H.HTMLEditorKit
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLEditorKit.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void read(Reader in, Document doc, int pos) throws IOException, BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_data parametro="Reader in" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_data parametro="Document doc" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [RuntimeException](/Java/RuntimeException/), [IOException](/Java/IOException/)

## Clase Padre
[HTMLEditorKit](/Java/HTMLEditorKit/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HTMLEditorKit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
