---
title: XMLSignatureFactory.newSignatureMethod()
permalink: /Java/XMLSignatureFactory/newSignatureMethod/
date: 2021-01-11
key: Java.X.XMLSignatureFactory
category: Java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newSignatureMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract SignatureMethod newSignatureMethod(String algorithm, SignatureMethodParameterSpec params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **SignatureMethodParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="SignatureMethodParameterSpec params" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [NullPointerException](/Java/NullPointerException/)

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
