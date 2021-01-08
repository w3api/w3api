---
title: XMLSignatureFactory.newCanonicalizationMethod()
permalink: Java/XMLSignatureFactory/newCanonicalizationMethod
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="newCanonicalizationMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CanonicalizationMethod newCanonicalizationMethod(String algorithm, C14NMethodParameterSpec params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
public abstract CanonicalizationMethod newCanonicalizationMethod(String algorithm, XMLStructure params) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **C14NMethodParameterSpec params**,  {% include w3api/param_description.html metodo=_data parametro="C14NMethodParameterSpec params" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **XMLStructure params**,  {% include w3api/param_description.html metodo=_data parametro="XMLStructure params" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

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
