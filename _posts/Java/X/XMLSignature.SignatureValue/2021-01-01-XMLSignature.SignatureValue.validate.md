---
title: XMLSignature.SignatureValue.validate()
permalink: /Java/XMLSignature/SignatureValue/validate/
date: 2021-01-11
key: Java.X.XMLSignature.SignatureValue
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignature.SignatureValue.metodos valor="validate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean validate(XMLValidateContext validateContext) throws XMLSignatureException
~~~

## Parámetros
* **XMLValidateContext validateContext**,  {% include w3api/param_description.html metodo=_dato parametro="XMLValidateContext validateContext" %}

## Excepciones
[XMLSignatureException](/Java/XMLSignatureException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignature.SignatureValue](/Java/XMLSignature/SignatureValue/)

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
