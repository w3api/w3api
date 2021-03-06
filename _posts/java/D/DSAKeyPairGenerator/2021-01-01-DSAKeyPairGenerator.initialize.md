---
title: DSAKeyPairGenerator.initialize()
permalink: /Java/DSAKeyPairGenerator/initialize/
date: 2021-01-11
key: Java.D.DSAKeyPairGenerator
category: Java
tags: ['java se', 'java.security.interfaces', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DSAKeyPairGenerator.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void initialize(int modlen, boolean genParams, SecureRandom random) throws InvalidParameterException
void initialize(DSAParams params, SecureRandom random) throws InvalidParameterException
~~~

## Parámetros
* **boolean genParams**,  {% include w3api/param_description.html metodo=_dato parametro="boolean genParams" %}
* **int modlen**,  {% include w3api/param_description.html metodo=_dato parametro="int modlen" %}
* **SecureRandom random**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandom random" %}
* **DSAParams params**,  {% include w3api/param_description.html metodo=_dato parametro="DSAParams params" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[DSAKeyPairGenerator](/Java/DSAKeyPairGenerator/)

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
