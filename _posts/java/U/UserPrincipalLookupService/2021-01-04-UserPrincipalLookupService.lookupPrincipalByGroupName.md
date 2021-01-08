---
title: UserPrincipalLookupService.lookupPrincipalByGroupName()
permalink: Java/UserPrincipalLookupService/lookupPrincipalByGroupName
date: 2021-01-04
key: JavaJava.U.UserPrincipalLookupService
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UserPrincipalLookupService.metodos valor="lookupPrincipalByGroupName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract GroupPrincipal lookupPrincipalByGroupName(String group) throws IOException
~~~

## Parámetros
* **String group**,  {% include w3api/param_description.html metodo=_data parametro="String group" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UserPrincipalNotFoundException](/Java/UserPrincipalNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[UserPrincipalLookupService](/Java/UserPrincipalLookupService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UserPrincipalLookupService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
