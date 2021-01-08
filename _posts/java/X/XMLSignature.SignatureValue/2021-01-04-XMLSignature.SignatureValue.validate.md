---
title: XMLSignature.SignatureValue.validate()
permalink: Java/XMLSignature/SignatureValue/validate
date: 2021-01-04
key: JavaJava.X.XMLSignature.SignatureValue
category: java
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
* **XMLValidateContext validateContext**,  {% include w3api/param_description.html metodo=_data parametro="XMLValidateContext validateContext" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [XMLSignatureException](/Java/XMLSignatureException/)

## Clase Padre
[XMLSignature.SignatureValue](/Java/XMLSignature/SignatureValue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLSignature.SignatureValue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
