---
title: HTMLEditorKit.InsertHTMLTextAction.insertAtBoundry()
permalink: Java/HTMLEditorKit/InsertHTMLTextAction/insertAtBoundry
date: 2021-01-11
key: JavaJava.H.HTMLEditorKit.InsertHTMLTextAction
category: java
tags: ['java se', 'javax.swing.text.html', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HTMLEditorKit.InsertHTMLTextAction.metodos valor="insertAtBoundry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated protected void insertAtBoundry(JEditorPane editor, HTMLDocument doc, int offset, Element insertElement, String html, HTML.Tag parentTag, HTML.Tag addTag)
~~~

## Parámetros
* **JEditorPane editor**,  {% include w3api/param_description.html metodo=_dato parametro="JEditorPane editor" %}
* **HTML.Tag parentTag**,  {% include w3api/param_description.html metodo=_dato parametro="HTML.Tag parentTag" %}
* **HTMLDocument doc**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLDocument doc" %}
* **HTML.Tag addTag**,  {% include w3api/param_description.html metodo=_dato parametro="HTML.Tag addTag" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **String html**,  {% include w3api/param_description.html metodo=_dato parametro="String html" %}
* **Element insertElement**,  {% include w3api/param_description.html metodo=_dato parametro="Element insertElement" %}

## Clase Padre
[HTMLEditorKit.InsertHTMLTextAction](/Java/HTMLEditorKit/InsertHTMLTextAction/)

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
