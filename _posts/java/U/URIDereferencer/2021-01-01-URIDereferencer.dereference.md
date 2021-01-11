---
title: URIDereferencer.dereference()
permalink: Java/URIDereferencer/dereference
date: 2021-01-11
key: JavaJava.U.URIDereferencer
category: java
tags: ['java se', 'javax.xml.crypto', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URIDereferencer.metodos valor="dereference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Data dereference(URIReference uriReference, XMLCryptoContext context) throws URIReferenceException
~~~

## Parámetros
* **URIReference uriReference**,  {% include w3api/param_description.html metodo=_dato parametro="URIReference uriReference" %}
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLCryptoContext context" %}

## Excepciones
[URIReferenceException](/Java/URIReferenceException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URIDereferencer](/Java/URIDereferencer/)

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
