---
title: PlainDocument.insertUpdate()
permalink: /Java/PlainDocument/insertUpdate/
date: 2021-01-11
key: Java.P.PlainDocument
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlainDocument.metodos valor="insertUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void insertUpdate(AbstractDocument.DefaultDocumentEvent chng, AttributeSet attr)
~~~

## Parámetros
* **AttributeSet attr**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeSet attr" %}
* **AbstractDocument.DefaultDocumentEvent chng**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractDocument.DefaultDocumentEvent chng" %}

## Clase Padre
[PlainDocument](/Java/PlainDocument/)

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
