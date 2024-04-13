---
title: RetrievalMethod.dereference()
permalink: /Java/RetrievalMethod/dereference/
date: 2021-01-11
key: Java.R.RetrievalMethod
category: Java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RetrievalMethod.metodos valor="dereference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Data dereference(XMLCryptoContext context) throws URIReferenceException
~~~

## Parámetros
* **XMLCryptoContext context**,  {% include w3api/param_description.html metodo=_dato parametro="XMLCryptoContext context" %}

## Excepciones
[URIReferenceException](/Java/URIReferenceException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[RetrievalMethod](/Java/RetrievalMethod/)

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
