---
title: AbstractWriter.AbstractWriter()
permalink: Java/AbstractWriter/AbstractWriter
date: 2021-01-11
key: JavaJava.A.AbstractWriter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractWriter.constructores valor="AbstractWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AbstractWriter(Writer w, Document doc)
protected AbstractWriter(Writer w, Document doc, int pos, int len)
protected AbstractWriter(Writer w, Element root)
protected AbstractWriter(Writer w, Element root, int pos, int len)
~~~

## Parámetros
* **Element root**,  {% include w3api/param_description.html metodo=_dato parametro="Element root" %}
* **Writer w**,  {% include w3api/param_description.html metodo=_dato parametro="Writer w" %}
* **int len**,  {% include w3api/param_description.html metodo=_dato parametro="int len" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_dato parametro="Document doc" %}
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Clase Padre
[AbstractWriter](/Java/AbstractWriter/)

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
