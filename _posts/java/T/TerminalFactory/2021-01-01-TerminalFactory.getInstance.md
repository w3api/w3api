---
title: TerminalFactory.getInstance()
permalink: /Java/TerminalFactory/getInstance/
date: 2021-01-11
key: Java.T.TerminalFactory
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TerminalFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TerminalFactory getInstance(String type, Object params) throws NoSuchAlgorithmException
public static TerminalFactory getInstance(String type, Object params, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static TerminalFactory getInstance(String type, Object params, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Object params**,  {% include w3api/param_description.html metodo=_dato parametro="Object params" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TerminalFactory](/Java/TerminalFactory/)

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
