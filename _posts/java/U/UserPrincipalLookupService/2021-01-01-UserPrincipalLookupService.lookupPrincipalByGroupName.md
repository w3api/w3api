---
title: UserPrincipalLookupService.lookupPrincipalByGroupName()
permalink: /Java/UserPrincipalLookupService/lookupPrincipalByGroupName/
date: 2021-01-11
key: Java.U.UserPrincipalLookupService
category: Java
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
* **String group**,  {% include w3api/param_description.html metodo=_dato parametro="String group" %}

## Excepciones
[UserPrincipalNotFoundException](/Java/UserPrincipalNotFoundException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[UserPrincipalLookupService](/Java/UserPrincipalLookupService/)

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
