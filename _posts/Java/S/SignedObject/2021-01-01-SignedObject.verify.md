---
title: SignedObject.verify()
permalink: /Java/SignedObject/verify/
date: 2021-01-11
key: Java.S.SignedObject
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignedObject.metodos valor="verify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean verify(PublicKey verificationKey, Signature verificationEngine) throws InvalidKeyException, SignatureException
~~~

## Parámetros
* **Signature verificationEngine**,  {% include w3api/param_description.html metodo=_dato parametro="Signature verificationEngine" %}
* **PublicKey verificationKey**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey verificationKey" %}

## Excepciones
[SignatureException](/Java/SignatureException/), [InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[SignedObject](/Java/SignedObject/)

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
