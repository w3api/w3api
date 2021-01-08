---
title: KeyInfoFactory.newX509IssuerSerial()
permalink: Java/KeyInfoFactory/newX509IssuerSerial
date: 2021-01-04
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newX509IssuerSerial" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract X509IssuerSerial newX509IssuerSerial(String issuerName, BigInteger serialNumber)
~~~

## Parámetros
* **BigInteger serialNumber**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger serialNumber" %}
* **String issuerName**,  {% include w3api/param_description.html metodo=_data parametro="String issuerName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyInfoFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
