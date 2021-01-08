---
title: RMISocketFactory.setSocketFactory()
permalink: Java/RMISocketFactory/setSocketFactory
date: 2021-01-04
key: JavaJava.R.RMISocketFactory
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMISocketFactory.metodos valor="setSocketFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setSocketFactory(RMISocketFactory fac) throws IOException
~~~

## Parámetros
* **RMISocketFactory fac**,  {% include w3api/param_description.html metodo=_data parametro="RMISocketFactory fac" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[RMISocketFactory](/Java/RMISocketFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMISocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
