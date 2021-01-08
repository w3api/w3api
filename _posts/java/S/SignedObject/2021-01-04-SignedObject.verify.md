---
title: SignedObject.verify()
permalink: Java/SignedObject/verify
date: 2021-01-04
key: JavaJava.S.SignedObject
category: java
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
* **PublicKey verificationKey**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey verificationKey" %}
* **Signature verificationEngine**,  {% include w3api/param_description.html metodo=_data parametro="Signature verificationEngine" %}

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
{%- for _ldc in site.data.Java.S.SignedObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
