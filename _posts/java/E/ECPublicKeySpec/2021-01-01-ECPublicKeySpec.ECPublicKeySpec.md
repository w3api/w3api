---
title: ECPublicKeySpec.ECPublicKeySpec()
permalink: /Java/ECPublicKeySpec/ECPublicKeySpec/
date: 2021-01-11
key: Java.E.ECPublicKeySpec
category: Java
tags: ['java se', 'java.security.spec', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ECPublicKeySpec.constructores valor="ECPublicKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ECPublicKeySpec(ECPoint w, ECParameterSpec params)
~~~

## Parámetros
* **ECPoint w**,  {% include w3api/param_description.html metodo=_dato parametro="ECPoint w" %}
* **ECParameterSpec params**,  {% include w3api/param_description.html metodo=_dato parametro="ECParameterSpec params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ECPublicKeySpec](/Java/ECPublicKeySpec/)

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
