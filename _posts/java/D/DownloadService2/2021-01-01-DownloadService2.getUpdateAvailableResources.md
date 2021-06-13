---
title: DownloadService2.getUpdateAvailableResources()
permalink: /Java/DownloadService2/getUpdateAvailableResources/
date: 2021-01-11
key: Java.D.DownloadService2
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', '6.0.18']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DownloadService2.metodos valor="getUpdateAvailableResources" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
DownloadService2.ResourceSpec[] getUpdateAvailableResources(DownloadService2.ResourceSpec spec) throws IOException
~~~

## Parámetros
* **DownloadService2.ResourceSpec spec**,  {% include w3api/param_description.html metodo=_dato parametro="DownloadService2.ResourceSpec spec" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[DownloadService2](/Java/DownloadService2/)

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
