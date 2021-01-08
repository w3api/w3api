---
title: PKIXParameters.PKIXParameters()
permalink: Java/PKIXParameters/PKIXParameters
date: 2021-01-04
key: JavaJava.P.PKIXParameters
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXParameters.constructores valor="PKIXParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKIXParameters(KeyStore keystore) throws KeyStoreException, InvalidAlgorithmParameterException
public PKIXParameters(Set<TrustAnchor> trustAnchors) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **KeyStore keystore**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore keystore" %}
* **Set&lt;TrustAnchor&gt; trustAnchors**,  {% include w3api/param_description.html metodo=_data parametro="Set<TrustAnchor> trustAnchors" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXParameters](/Java/PKIXParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PKIXParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
