---
title: HTMLEditorKit.InsertHTMLTextAction.insertHTML()
permalink: Java/HTMLEditorKit/InsertHTMLTextAction/insertHTML
date: 2021-01-04
key: JavaJava.H.HTMLEditorKit.InsertHTMLTextAction
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLEditorKit.InsertHTMLTextAction.metodos valor="insertHTML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void insertHTML(JEditorPane editor, HTMLDocument doc, int offset, String html, int popDepth, int pushDepth, HTML.Tag addTag)
~~~

## Parámetros
* **HTML.Tag addTag**,  {% include w3api/param_description.html metodo=_data parametro="HTML.Tag addTag" %}
* **int popDepth**,  {% include w3api/param_description.html metodo=_data parametro="int popDepth" %}
* **int pushDepth**,  {% include w3api/param_description.html metodo=_data parametro="int pushDepth" %}
* **HTMLDocument doc**,  {% include w3api/param_description.html metodo=_data parametro="HTMLDocument doc" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **JEditorPane editor**,  {% include w3api/param_description.html metodo=_data parametro="JEditorPane editor" %}
* **String html**,  {% include w3api/param_description.html metodo=_data parametro="String html" %}

## Clase Padre
[HTMLEditorKit.InsertHTMLTextAction](/Java/HTMLEditorKit/InsertHTMLTextAction/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HTMLEditorKit.InsertHTMLTextAction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
