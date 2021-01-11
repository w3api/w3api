---
title: X500PrivateCredential.X500PrivateCredential()
permalink: Java/X500PrivateCredential/X500PrivateCredential
date: 2021-01-11
key: JavaJava.X.X500PrivateCredential
category: java
tags: ['java se', 'javax.security.auth.x500', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X500PrivateCredential.constructores valor="X500PrivateCredential" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public X500PrivateCredential(X509Certificate cert, PrivateKey key)
public X500PrivateCredential(X509Certificate cert, PrivateKey key, String alias)
~~~

## Parámetros
* **PrivateKey key**,  {% include w3api/param_description.html metodo=_dato parametro="PrivateKey key" %}
* **X509Certificate cert**,  {% include w3api/param_description.html metodo=_dato parametro="X509Certificate cert" %}
* **String alias**,  {% include w3api/param_description.html metodo=_dato parametro="String alias" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[X500PrivateCredential](/Java/X500PrivateCredential/)

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
