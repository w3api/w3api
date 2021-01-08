---
title: XMLSignatureFactory.newXMLSignature()
permalink: Java/XMLSignatureFactory/newXMLSignature
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newXMLSignature" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLSignature newXMLSignature(SignedInfo si, KeyInfo ki)
public abstract XMLSignature newXMLSignature(SignedInfo si, KeyInfo ki, List<? extends XMLObject> objects, String id, String signatureValueId)
~~~

## Parámetros
* **List&lt;? extends XMLObject&gt; objects**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends XMLObject> objects" %}
* **String signatureValueId**,  {% include w3api/param_description.html metodo=_data parametro="String signatureValueId" %}
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **SignedInfo si**,  {% include w3api/param_description.html metodo=_data parametro="SignedInfo si" %}
* **KeyInfo ki**,  {% include w3api/param_description.html metodo=_data parametro="KeyInfo ki" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XMLSignatureFactory](/Java/XMLSignatureFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLSignatureFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
