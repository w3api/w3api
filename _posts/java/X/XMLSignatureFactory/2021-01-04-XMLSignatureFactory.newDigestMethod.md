---
title: XMLSignatureFactory.newDigestMethod()
permalink: Java/XMLSignatureFactory/newDigestMethod
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newDigestMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract DigestMethod newDigestMethod(String algorithm, DigestMethodParameterSpec params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **DigestMethodParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="DigestMethodParameterSpec params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [NullPointerException](/Java/NullPointerException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

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
