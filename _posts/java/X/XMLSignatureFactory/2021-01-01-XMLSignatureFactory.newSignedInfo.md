---
title: XMLSignatureFactory.newSignedInfo()
permalink: /Java/XMLSignatureFactory/newSignedInfo/
date: 2021-01-11
key: Java.X.XMLSignatureFactory
category: Java
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
* **CanonicalizationMethod cm**,  {% include w3api/param_description.html metodo=_dato parametro="CanonicalizationMethod cm" %}
* **SignatureMethod sm**,  {% include w3api/param_description.html metodo=_dato parametro="SignatureMethod sm" %}
* **List&lt;? extends Reference&gt; references**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Reference> references" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}

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
