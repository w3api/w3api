---
title: DownloadServiceListener
permalink: Java/DownloadServiceListener
date: 2021-01-11
key: JavaJava.D.DownloadServiceListener
category: java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'interface java', 'Java 1.4.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DownloadServiceListener.description }}

## Sintaxis
~~~java
public interface DownloadServiceListener
~~~

## Métodos
* [downloadFailed()](/Java/DownloadServiceListener/downloadFailed)
* [progress()](/Java/DownloadServiceListener/progress)
* [upgradingArchive()](/Java/DownloadServiceListener/upgradingArchive)
* [validating()](/Java/DownloadServiceListener/validating)

## Ejemplo
~~~java
{{ site.data.Java.D.DownloadServiceListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DownloadServiceListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
