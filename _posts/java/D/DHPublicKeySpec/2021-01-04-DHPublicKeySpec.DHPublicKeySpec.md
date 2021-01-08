---
title: DHPublicKeySpec.DHPublicKeySpec()
permalink: Java/DHPublicKeySpec/DHPublicKeySpec
date: 2021-01-04
key: JavaJava.D.DHPublicKeySpec
category: java
tags: ['java se', 'javax.crypto.spec', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DHPublicKeySpec.constructores valor="DHPublicKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DHPublicKeySpec(BigInteger y, BigInteger p, BigInteger g)
~~~

## Parámetros
* **BigInteger p**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger p" %}
* **BigInteger y**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger y" %}
* **BigInteger g**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger g" %}

## Clase Padre
[DHPublicKeySpec](/Java/DHPublicKeySpec/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DHPublicKeySpec.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
