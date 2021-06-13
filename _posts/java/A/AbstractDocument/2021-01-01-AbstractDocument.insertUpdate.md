---
title: AbstractDocument.insertUpdate()
permalink: /Java/AbstractDocument/insertUpdate/
date: 2021-01-11
key: Java.A.AbstractDocument
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractDocument.metodos valor="insertUpdate" %}

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
[AbstractDocument](/Java/AbstractDocument/)

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
