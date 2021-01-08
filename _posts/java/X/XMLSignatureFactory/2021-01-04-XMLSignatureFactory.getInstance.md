---
title: XMLSignatureFactory.getInstance()
permalink: Java/XMLSignatureFactory/getInstance
date: 2021-01-04
key: JavaJava.X.XMLSignatureFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLSignatureFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static XMLSignatureFactory getInstance()
public static XMLSignatureFactory getInstance(String mechanismType)
public static XMLSignatureFactory getInstance(String mechanismType, String provider) throws NoSuchProviderException
public static XMLSignatureFactory getInstance(String mechanismType, Provider provider)
~~~

## Parámetros
* **String mechanismType**,  {% include w3api/param_description.html metodo=_data parametro="String mechanismType" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [NoSuchMechanismException](/Java/NoSuchMechanismException/)

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
