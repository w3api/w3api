---
title: ECPrivateKeySpec.ECPrivateKeySpec()
permalink: /Java/ECPrivateKeySpec/ECPrivateKeySpec/
date: 2021-01-11
key: Java.E.ECPrivateKeySpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ECPrivateKeySpec.constructores valor="ECPrivateKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ECPrivateKeySpec(BigInteger s, ECParameterSpec params)
~~~

## Parámetros
* **BigInteger s**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger s" %}
* **ECParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="ECParameterSpec params" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ECPrivateKeySpec](/Java/ECPrivateKeySpec/)

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
