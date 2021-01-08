---
title: KeyAgreement.KeyAgreement()
permalink: Java/KeyAgreement/KeyAgreement
date: 2021-01-04
key: JavaJava.K.KeyAgreement
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreement.constructores valor="KeyAgreement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected KeyAgreement(KeyAgreementSpi keyAgreeSpi, Provider provider, String algorithm)
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **KeyAgreementSpi keyAgreeSpi**,  {% include w3api/param_description.html metodo=_data parametro="KeyAgreementSpi keyAgreeSpi" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}

## Clase Padre
[KeyAgreement](/Java/KeyAgreement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyAgreement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
