---
title: MinimalHTMLWriter.writeContent()
permalink: /Java/MinimalHTMLWriter/writeContent/
date: 2021-01-11
key: Java.M.MinimalHTMLWriter
category: Java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinimalHTMLWriter.metodos valor="writeContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void writeContent(Element elem, boolean needsIndenting) throws IOException, BadLocationException
~~~

## Parámetros
* **Element elem**,  {% include w3api/param_description.html metodo=_dato parametro="Element elem" %}
* **boolean needsIndenting**,  {% include w3api/param_description.html metodo=_dato parametro="boolean needsIndenting" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[MinimalHTMLWriter](/Java/MinimalHTMLWriter/)

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
