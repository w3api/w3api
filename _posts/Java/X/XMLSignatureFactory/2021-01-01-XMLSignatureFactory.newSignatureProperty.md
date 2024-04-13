---
title: XMLSignatureFactory.newSignatureProperty()
permalink: /Java/XMLSignatureFactory/newSignatureProperty/
date: 2021-01-11
key: Java.X.XMLSignatureFactory
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newSignatureProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SignatureProperty newSignatureProperty(List<? extends XMLStructure> content, String target, String id)
~~~

## Parámetros
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **List&lt;? extends XMLStructure&gt; content**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends XMLStructure> content" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

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
