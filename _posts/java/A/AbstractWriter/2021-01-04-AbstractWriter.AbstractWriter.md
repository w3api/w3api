---
title: AbstractWriter.AbstractWriter()
permalink: Java/AbstractWriter/AbstractWriter
date: 2021-01-04
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
* **Element root**,  {% include w3api/param_description.html metodo=_data parametro="Element root" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Writer w**,  {% include w3api/param_description.html metodo=_data parametro="Writer w" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_data parametro="Document doc" %}

## Clase Padre
[AbstractWriter](/Java/AbstractWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
