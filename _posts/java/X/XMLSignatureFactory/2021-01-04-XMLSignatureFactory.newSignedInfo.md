---
title: XMLSignatureFactory.newSignedInfo()
permalink: Java/XMLSignatureFactory/newSignedInfo
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newSignedInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SignedInfo newSignedInfo(CanonicalizationMethod cm, SignatureMethod sm, List<? extends Reference> references)
public abstract SignedInfo newSignedInfo(CanonicalizationMethod cm, SignatureMethod sm, List<? extends Reference> references, String id)
~~~

## Parámetros
* **SignatureMethod sm**,  {% include w3api/param_description.html metodo=_data parametro="SignatureMethod sm" %}
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **CanonicalizationMethod cm**,  {% include w3api/param_description.html metodo=_data parametro="CanonicalizationMethod cm" %}
* **List&lt;? extends Reference&gt; references**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Reference> references" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
