---
title: KeyInfoFactory.getInstance()
permalink: /Java/KeyInfoFactory/getInstance/
date: 2021-01-11
key: Java.K.KeyInfoFactory
category: Java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static KeyInfoFactory getInstance()
public static KeyInfoFactory getInstance(String mechanismType)
public static KeyInfoFactory getInstance(String mechanismType, String provider) throws NoSuchProviderException
public static KeyInfoFactory getInstance(String mechanismType, Provider provider)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **String mechanismType**,  {% include w3api/param_description.html metodo=_dato parametro="String mechanismType" %}

## Excepciones
[NoSuchMechanismException](/Java/NoSuchMechanismException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

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
