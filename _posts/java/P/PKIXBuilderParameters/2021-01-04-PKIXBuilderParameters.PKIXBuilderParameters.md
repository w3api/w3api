---
title: PKIXBuilderParameters.PKIXBuilderParameters()
permalink: Java/PKIXBuilderParameters/PKIXBuilderParameters
date: 2021-01-04
key: JavaJava.P.PKIXBuilderParameters
category: java
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
* **KeyStore keystore**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore keystore" %}
* **CertSelector targetConstraints**,  {% include w3api/param_description.html metodo=_data parametro="CertSelector targetConstraints" %}
* **Set&lt;TrustAnchor&gt; trustAnchors**,  {% include w3api/param_description.html metodo=_data parametro="Set<TrustAnchor> trustAnchors" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKIXBuilderParameters](/Java/PKIXBuilderParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PKIXBuilderParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
