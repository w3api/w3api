---
title: AclFileAttributeView.setAcl()
permalink: /Java/AclFileAttributeView/setAcl/
date: 2021-01-11
key: Java.A.AclFileAttributeView
category: Java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AclFileAttributeView.metodos valor="setAcl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAcl(List<AclEntry> acl) throws IOException
~~~

## Parámetros
* **List&lt;AclEntry&gt; acl**,  {% include w3api/param_description.html metodo=_dato parametro="List<AclEntry> acl" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[AclFileAttributeView](/Java/AclFileAttributeView/)

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
