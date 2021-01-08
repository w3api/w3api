---
title: Reference.validate()
permalink: Java/Reference-javax-xml-crypto-dsig/validate
date: 2021-01-04
key: JavaJava.R.Reference-javax-xml-crypto-dsig
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Reference-javax-xml-crypto-dsig.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean validate(XMLValidateContext validateContext) throws XMLSignatureException
~~~

## Parámetros
* **XMLValidateContext validateContext**,  {% include w3api/param_description.html metodo=_data parametro="XMLValidateContext validateContext" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [XMLSignatureException](/Java/XMLSignatureException/)

## Clase Padre
[Reference](/Java/Reference-javax-xml-crypto-dsig/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Reference-javax-xml-crypto-dsig.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
