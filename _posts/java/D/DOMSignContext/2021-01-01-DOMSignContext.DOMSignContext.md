---
title: DOMSignContext.DOMSignContext()
permalink: Java/DOMSignContext/DOMSignContext
date: 2021-01-11
key: JavaJava.D.DOMSignContext
category: java
tags: ['java se', 'javax.xml.crypto.dsig.dom', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMSignContext.constructores valor="DOMSignContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DOMSignContext(Key signingKey, Node parent)
public DOMSignContext(Key signingKey, Node parent, Node nextSibling)
public DOMSignContext(KeySelector ks, Node parent)
public DOMSignContext(KeySelector ks, Node parent, Node nextSibling)
~~~

## Parámetros
* **Key signingKey**,  {% include w3api/param_description.html metodo=_dato parametro="Key signingKey" %}
* **KeySelector ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeySelector ks" %}
* **Node parent**,  {% include w3api/param_description.html metodo=_dato parametro="Node parent" %}
* **Node nextSibling**,  {% include w3api/param_description.html metodo=_dato parametro="Node nextSibling" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DOMSignContext](/Java/DOMSignContext/)

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
