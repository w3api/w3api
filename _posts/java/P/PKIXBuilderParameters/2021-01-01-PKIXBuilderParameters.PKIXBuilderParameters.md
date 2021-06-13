---
title: PKIXBuilderParameters.PKIXBuilderParameters()
permalink: /Java/PKIXBuilderParameters/PKIXBuilderParameters/
date: 2021-01-11
key: Java.P.PKIXBuilderParameters
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXBuilderParameters.constructores valor="PKIXBuilderParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKIXBuilderParameters(KeyStore keystore, CertSelector targetConstraints) throws KeyStoreException, InvalidAlgorithmParameterException
public PKIXBuilderParameters(Set<TrustAnchor> trustAnchors, CertSelector targetConstraints) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **Set&lt;TrustAnchor&gt; trustAnchors**,  {% include w3api/param_description.html metodo=_dato parametro="Set<TrustAnchor> trustAnchors" %}
* **CertSelector targetConstraints**,  {% include w3api/param_description.html metodo=_dato parametro="CertSelector targetConstraints" %}
* **KeyStore keystore**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore keystore" %}

## Excepciones
[InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [KeyStoreException](/Java/KeyStoreException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXBuilderParameters](/Java/PKIXBuilderParameters/)

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
