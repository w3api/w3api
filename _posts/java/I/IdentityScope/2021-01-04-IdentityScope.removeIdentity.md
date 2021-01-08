---
title: IdentityScope.removeIdentity()
permalink: Java/IdentityScope/removeIdentity
date: 2021-01-04
key: JavaJava.I.IdentityScope
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityScope.metodos valor="removeIdentity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void removeIdentity(Identity identity) throws KeyManagementException
~~~

## Parámetros
* **Identity identity**,  {% include w3api/param_description.html metodo=_data parametro="Identity identity" %}

## Excepciones
[KeyManagementException](/Java/KeyManagementException/)

## Clase Padre
[IdentityScope](/Java/IdentityScope/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IdentityScope.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
